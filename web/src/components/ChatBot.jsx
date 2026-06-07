import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";

import {
  MessageSquare,
  X,
  Send,
  Loader2,
  ShoppingCart,
  Trash2,
  Sparkles,
} from "lucide-react";
import useChat from "@/hooks/useChat";

const SAMPLE_PROMPTS = [
  "Show me red and blue shirts for a beach trip",
  "Best running shoes under $130",
  "I need a jacket for rainy weather",
  "What casual pants do you have?",
];

export default function ChatBot({ defaultOpen = false }) {
  const [isOpen, setIsOpen] = useState(defaultOpen);
  const [input, setInput] = useState("");
  const { messages, isLoading, sendMessage, clearChat } = useChat();
  const scrollRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);

  const handleSend = () => {
    const text = input.trim();
    if (!text || isLoading) return;
    setInput("");
    sendMessage(text);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handlePromptClick = (prompt) => {
    sendMessage(prompt);
  };

  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 right-6 z-50 w-14 h-14 rounded-full bg-primary text-primary-foreground flex items-center justify-center shadow-lg hover:scale-110 transition-transform glow cursor-pointer"
        aria-label="Open chat"
      >
        <MessageSquare className="w-6 h-6" />
      </button>
    );
  }

  return (
    <div className="fixed bottom-6 right-6 z-50 w-[400px] max-w-[calc(100vw-2rem)] h-[560px] max-h-[calc(100vh-3rem)] rounded-2xl border border-border/60 bg-card shadow-2xl flex flex-col overflow-hidden animate-in fade-in slide-in-from-bottom-4 zoom-in-95 duration-300">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-border/50 bg-secondary/30">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
            <ShoppingCart className="w-4 h-4 text-primary-foreground" />
          </div>
          <div>
            <p className="text-sm font-semibold leading-tight">SmartCart Assistant</p>
            <p className="text-[11px] text-muted-foreground flex items-center gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-green-500 inline-block" />
              Online
            </p>
          </div>
        </div>
        <div className="flex items-center gap-1">
          <Button
            variant="ghost"
            size="icon"
            className="h-7 w-7"
            onClick={clearChat}
            title="Clear chat"
          >
            <Trash2 className="w-3.5 h-3.5" />
          </Button>
          <Button
            variant="ghost"
            size="icon"
            className="h-7 w-7"
            onClick={() => setIsOpen(false)}
          >
            <X className="w-4 h-4" />
          </Button>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 min-h-0 overflow-y-auto px-4 scrollbar-hide" ref={scrollRef}>
        <div className="py-4 space-y-4">
          {messages.length === 0 && (
            <div className="space-y-4">
              <div className="text-center py-4">
                <div className="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center mx-auto mb-3">
                  <Sparkles className="w-6 h-6 text-primary" />
                </div>
                <p className="text-sm font-medium mb-1">Hi! I'm your shopping assistant</p>
                <p className="text-xs text-muted-foreground">
                  Ask me anything about our products
                </p>
              </div>
              <div className="space-y-2">
                <p className="text-[11px] text-muted-foreground font-medium uppercase tracking-wider">
                  Try asking
                </p>
                {SAMPLE_PROMPTS.map((prompt) => (
                  <button
                    key={prompt}
                    onClick={() => handlePromptClick(prompt)}
                    className="w-full text-left text-xs px-3 py-2 rounded-lg border border-border/50 bg-secondary/30 hover:bg-secondary/60 hover:border-primary/30 transition-all cursor-pointer"
                  >
                    &ldquo;{prompt}&rdquo;
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((msg, i) => (
            <div
              key={i}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
            >
              <div
                className={`max-w-[85%] rounded-2xl px-3.5 py-2.5 text-sm leading-relaxed ${
                  msg.role === "user"
                    ? "bg-primary text-primary-foreground rounded-br-md"
                    : "bg-secondary/60 text-foreground rounded-bl-md"
                }`}
              >
                <p className="whitespace-pre-wrap">{msg.content}</p>
                {msg.products && msg.products.length > 0 && (
                  <div className="mt-2 pt-2 border-t border-border/30 flex flex-wrap gap-1">
                    {msg.products.slice(0, 4).map((p) => (
                      <Badge
                        key={p.id}
                        variant="outline"
                        className="text-[10px] px-1.5 py-0"
                      >
                        {p.name} · ${p.price}
                      </Badge>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-secondary/60 rounded-2xl rounded-bl-md px-4 py-3">
                <Loader2 className="w-4 h-4 animate-spin text-muted-foreground" />
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Input */}
      <div className="p-3 border-t border-border/50">
        <div className="flex gap-2">
          <Input
            ref={inputRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask about products..."
            className="text-sm h-9"
            disabled={isLoading}
          />
          <Button
            size="icon"
            className="h-9 w-9 shrink-0"
            onClick={handleSend}
            disabled={isLoading || !input.trim()}
          >
            <Send className="w-4 h-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}
