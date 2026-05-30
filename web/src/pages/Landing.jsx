import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import {
  Sparkles,
  Phone,
  ShoppingBag,
  MessageSquare,
  Zap,
  Shield,
  ArrowRight,
} from "lucide-react";

const FEATURES = [
  {
    icon: MessageSquare,
    title: "Natural Conversations",
    desc: "AI that understands context, handles follow-ups, and recommends like a real shopping expert.",
  },
  {
    icon: Zap,
    title: "Plug & Play",
    desc: "Integrate with any e-commerce platform. Just expose your inventory and connect our API.",
  },
  {
    icon: Shield,
    title: "Your LLM, Your Rules",
    desc: "Choose between OpenAI, Gemini, or bring your own. Full control over provider, model, and keys.",
  },
  {
    icon: ShoppingBag,
    title: "Inventory-Aware",
    desc: "RAG-powered retrieval ensures recommendations are always from your real, in-stock catalog.",
  },
];

export default function Landing() {
  return (
    <main>
      {/* Hero */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-16">
        {/* Background effects */}
        <div className="absolute inset-0 gradient-bg" />
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[600px] h-[600px] rounded-full bg-primary/5 blur-[120px]" />

        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-border/60 bg-secondary/50 text-sm text-muted-foreground mb-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <Sparkles className="w-3.5 h-3.5 text-primary" />
            AI-Powered Shopping Assistant
          </div>

          <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold tracking-tight leading-[1.1] mb-6 animate-in fade-in slide-in-from-bottom-6 duration-700 delay-100">
            Turn Browsers Into{" "}
            <span className="gradient-text">Buyers</span>
          </h1>

          <p className="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto mb-10 leading-relaxed animate-in fade-in slide-in-from-bottom-8 duration-700 delay-200">
            SmartCart is a RAG-based virtual shopping assistant that plugs into
            any e-commerce store. It understands your inventory, talks to your
            customers, and helps them find exactly what they need.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 animate-in fade-in slide-in-from-bottom-10 duration-700 delay-300">
            <Link to="/demo">
              <Button size="lg" className="gap-2 text-base px-8 h-12 glow">
                <Sparkles className="w-4 h-4" />
                See Demo
              </Button>
            </Link>
            <Link to="/contact">
              <Button
                variant="outline"
                size="lg"
                className="gap-2 text-base px-8 h-12"
              >
                <Phone className="w-4 h-4" />
                Book a Call
              </Button>
            </Link>
          </div>

          {/* Floating indicators */}
          <div className="mt-16 flex items-center justify-center gap-8 text-sm text-muted-foreground animate-in fade-in duration-1000 delay-500">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
              Multi-LLM Support
            </div>
            <div className="hidden sm:flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-blue-500 animate-pulse" />
              Real-time Inventory
            </div>
            <div className="hidden md:flex items-center gap-2">
              <div className="w-2 h-2 rounded-full bg-purple-500 animate-pulse" />
              Plug & Play API
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-24 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mb-4">
              Built for Modern E-Commerce
            </h2>
            <p className="text-muted-foreground max-w-xl mx-auto">
              Everything you need to add an intelligent shopping assistant to
              your store — without building one from scratch.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {FEATURES.map((f, i) => (
              <div
                key={f.title}
                className="group p-6 rounded-2xl border border-border/50 bg-card/40 hover:bg-card/80 hover:border-primary/30 transition-all duration-300 hover:-translate-y-1"
                style={{ animationDelay: `${i * 100}ms` }}
              >
                <div className="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                  <f.icon className="w-5 h-5 text-primary" />
                </div>
                <h3 className="font-semibold mb-2">{f.title}</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  {f.desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 px-6">
        <div className="max-w-3xl mx-auto text-center glass rounded-3xl p-12 glow">
          <h2 className="text-3xl font-bold tracking-tight mb-4">
            Ready to Supercharge Your Store?
          </h2>
          <p className="text-muted-foreground mb-8 max-w-lg mx-auto">
            See how SmartCart handles real shopping conversations. Try the live
            demo with our mock clothing store.
          </p>
          <Link to="/demo">
            <Button size="lg" className="gap-2 text-base px-8 h-12">
              Launch Demo
              <ArrowRight className="w-4 h-4" />
            </Button>
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border/50 py-8 px-6">
        <div className="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-muted-foreground">
          <span>© 2025 SmartCart. Built with RAG.</span>
          <div className="flex gap-6">
            <Link to="/" className="hover:text-foreground transition-colors">
              Home
            </Link>
            <Link
              to="/demo"
              className="hover:text-foreground transition-colors"
            >
              Demo
            </Link>
            <Link
              to="/contact"
              className="hover:text-foreground transition-colors"
            >
              Contact
            </Link>
          </div>
        </div>
      </footer>
    </main>
  );
}
