import { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import {
  ShoppingCart,
  ArrowLeft,
  Search,
} from "lucide-react";
import ProductGrid from "@/components/ProductGrid";
import ChatBot from "@/components/ChatBot";
import MOCK_PRODUCTS from "@/data/mockProducts";

const CATEGORIES = ["All", ...new Set(MOCK_PRODUCTS.map((p) => p.category))];

export default function Demo() {
  const [activeCategory, setActiveCategory] = useState("All");
  const [search, setSearch] = useState("");

  const filtered = MOCK_PRODUCTS.filter((p) => {
    const matchCategory =
      activeCategory === "All" || p.category === activeCategory;
    const matchSearch =
      !search ||
      p.name.toLowerCase().includes(search.toLowerCase()) ||
      p.description.toLowerCase().includes(search.toLowerCase());
    return matchCategory && matchSearch;
  });

  return (
    <div className="min-h-screen bg-background">
      {/* Demo store navbar */}
      <nav className="sticky top-0 z-40 glass">
        <div className="max-w-7xl mx-auto px-6 h-14 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link
              to="/"
              className="text-muted-foreground hover:text-foreground transition-colors"
              title="Back to SmartCart"
            >
              <ArrowLeft className="w-4 h-4" />
            </Link>
            <div className="flex items-center gap-2">
              <ShoppingCart className="w-5 h-5 text-primary" />
              <span className="font-semibold text-sm">ThreadHaven</span>
              <Badge variant="outline" className="text-[10px] px-1.5 py-0 ml-1">
                Demo Store
              </Badge>
            </div>
          </div>

          <div className="hidden sm:flex items-center gap-2 flex-1 max-w-xs ml-6">
            <div className="relative w-full">
              <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-muted-foreground" />
              <Input
                placeholder="Search products..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="h-8 text-xs pl-8"
              />
            </div>
          </div>
        </div>
      </nav>

      {/* Store content */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        {/* Hero banner */}
        <div className="rounded-2xl gradient-bg border border-border/30 p-8 mb-8">
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight mb-2">
            Welcome to ThreadHaven
          </h1>
          <p className="text-muted-foreground text-sm max-w-xl mb-4">
            Explore our curated collection of clothing and accessories. Need
            help finding something? Use the AI assistant in the bottom-right
            corner!
          </p>
          <div className="flex items-center gap-2 text-xs text-muted-foreground">
            <div className="w-2 h-2 rounded-full bg-primary animate-pulse" />
            SmartCart AI Assistant is active — try asking it a question
          </div>
        </div>

        {/* Category filters */}
        <div className="flex items-center gap-2 mb-6 overflow-x-auto pb-2">
          {CATEGORIES.map((cat) => (
            <Button
              key={cat}
              variant={activeCategory === cat ? "default" : "outline"}
              size="sm"
              className="text-xs shrink-0"
              onClick={() => setActiveCategory(cat)}
            >
              {cat}
            </Button>
          ))}
        </div>

        {/* Product grid */}
        {filtered.length > 0 ? (
          <ProductGrid products={filtered} />
        ) : (
          <div className="text-center py-16 text-muted-foreground">
            <p className="text-sm">No products found. Try a different filter.</p>
          </div>
        )}

        {/* Bottom spacer for chatbot */}
        <div className="h-20" />
      </main>

      {/* Chatbot — open by default */}
      <ChatBot defaultOpen={true} />
    </div>
  );
}
