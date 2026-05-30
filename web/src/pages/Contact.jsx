import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { ArrowLeft, Mail, Send, CheckCircle } from "lucide-react";
import { Link } from "react-router-dom";

export default function Contact() {
  const [submitted, setSubmitted] = useState(false);
  const [form, setForm] = useState({
    name: "",
    email: "",
    company: "",
    message: "",
  });

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const subject = encodeURIComponent(
      `SmartCart Inquiry from ${form.name} — ${form.company}`
    );
    const body = encodeURIComponent(
      `Name: ${form.name}\nEmail: ${form.email}\nCompany: ${form.company}\n\n${form.message}`
    );
    window.location.href = `mailto:hello@smartcart.dev?subject=${subject}&body=${body}`;
    setSubmitted(true);
  };

  return (
    <main className="min-h-screen flex items-center justify-center px-6 pt-24 pb-12">
      <div className="w-full max-w-lg">
        <Link
          to="/"
          className="inline-flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground transition-colors mb-8"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Home
        </Link>

        {submitted ? (
          <div className="glass rounded-2xl p-10 text-center animate-in fade-in zoom-in-95 duration-500">
            <div className="w-16 h-16 rounded-full bg-green-500/10 flex items-center justify-center mx-auto mb-6">
              <CheckCircle className="w-8 h-8 text-green-500" />
            </div>
            <h2 className="text-2xl font-bold mb-2">Email Client Opened!</h2>
            <p className="text-muted-foreground mb-6">
              Your email client should have opened with the pre-filled message.
              Send it and we&apos;ll get back to you within 24 hours.
            </p>
            <Button variant="outline" onClick={() => setSubmitted(false)}>
              Send Another
            </Button>
          </div>
        ) : (
          <div className="glass rounded-2xl p-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center">
                <Mail className="w-5 h-5 text-primary" />
              </div>
              <div>
                <h1 className="text-2xl font-bold">Book a Call</h1>
                <p className="text-sm text-muted-foreground">
                  Tell us about your use case
                </p>
              </div>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label
                    htmlFor="name"
                    className="text-sm font-medium mb-1.5 block"
                  >
                    Name
                  </label>
                  <Input
                    id="name"
                    name="name"
                    placeholder="Your name"
                    value={form.name}
                    onChange={handleChange}
                    required
                  />
                </div>
                <div>
                  <label
                    htmlFor="email"
                    className="text-sm font-medium mb-1.5 block"
                  >
                    Email
                  </label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    placeholder="you@company.com"
                    value={form.email}
                    onChange={handleChange}
                    required
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="company"
                  className="text-sm font-medium mb-1.5 block"
                >
                  Company
                </label>
                <Input
                  id="company"
                  name="company"
                  placeholder="Your company name"
                  value={form.company}
                  onChange={handleChange}
                />
              </div>

              <div>
                <label
                  htmlFor="message"
                  className="text-sm font-medium mb-1.5 block"
                >
                  Message
                </label>
                <Textarea
                  id="message"
                  name="message"
                  placeholder="Tell us about your e-commerce platform and how you'd like to use SmartCart..."
                  rows={4}
                  value={form.message}
                  onChange={handleChange}
                  required
                />
              </div>

              <Button type="submit" className="w-full gap-2 h-11">
                <Send className="w-4 h-4" />
                Send Message
              </Button>
            </form>
          </div>
        )}
      </div>
    </main>
  );
}
