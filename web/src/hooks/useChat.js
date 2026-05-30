import { useState, useCallback } from "react";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";
const TENANT_ID = "demo";

export default function useChat() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = useCallback(
    async (text) => {
      const userMsg = { role: "user", content: text };
      setMessages((prev) => [...prev, userMsg]);
      setIsLoading(true);
      setError(null);

      const history = messages.map((m) => ({
        role: m.role,
        content: m.content,
      }));

      try {
        const res = await fetch(`${API_BASE}/api/v1/chat`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            tenant_id: TENANT_ID,
            message: text,
            conversation_history: history,
          }),
        });

        if (!res.ok) throw new Error(`Server error: ${res.status}`);

        const data = await res.json();
        const assistantMsg = {
          role: "assistant",
          content: data.reply,
          products: data.products || [],
        };
        setMessages((prev) => [...prev, assistantMsg]);
      } catch (err) {
        setError(err.message);
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content:
              "Sorry, I'm having trouble connecting right now. Please make sure the backend server is running.",
          },
        ]);
      } finally {
        setIsLoading(false);
      }
    },
    [messages]
  );

  const clearChat = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return { messages, isLoading, error, sendMessage, clearChat };
}
