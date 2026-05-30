import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger, SheetTitle } from "@/components/ui/sheet";
import { Menu, ShoppingCart, Sparkles } from "lucide-react";

const NAV_LINKS = [
  { label: "Home", href: "/" },
  { label: "Demo", href: "/demo" },
  { label: "Contact", href: "/contact" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const location = useLocation();

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 glass">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2 group">
          <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center group-hover:scale-110 transition-transform">
            <ShoppingCart className="w-4 h-4 text-primary-foreground" />
          </div>
          <span className="text-lg font-semibold tracking-tight">SmartCart</span>
        </Link>

        <div className="hidden md:flex items-center gap-1">
          {NAV_LINKS.map((link) => (
            <Link key={link.href} to={link.href}>
              <Button
                variant={location.pathname === link.href ? "secondary" : "ghost"}
                size="sm"
                className="text-sm"
              >
                {link.label}
              </Button>
            </Link>
          ))}
          <Link to="/demo" className="ml-2">
            <Button size="sm" className="gap-1.5">
              <Sparkles className="w-3.5 h-3.5" />
              Try Demo
            </Button>
          </Link>
        </div>

        <Sheet open={open} onOpenChange={setOpen}>
          <SheetTrigger asChild className="md:hidden">
            <Button variant="ghost" size="icon">
              <Menu className="w-5 h-5" />
            </Button>
          </SheetTrigger>
          <SheetContent side="right" className="w-72">
            <SheetTitle className="sr-only">Navigation Menu</SheetTitle>
            <div className="flex flex-col gap-2 mt-8">
              {NAV_LINKS.map((link) => (
                <Link key={link.href} to={link.href} onClick={() => setOpen(false)}>
                  <Button
                    variant={location.pathname === link.href ? "secondary" : "ghost"}
                    className="w-full justify-start"
                  >
                    {link.label}
                  </Button>
                </Link>
              ))}
              <Link to="/demo" onClick={() => setOpen(false)}>
                <Button className="w-full gap-1.5 mt-2">
                  <Sparkles className="w-3.5 h-3.5" />
                  Try Demo
                </Button>
              </Link>
            </div>
          </SheetContent>
        </Sheet>
      </div>
    </nav>
  );
}
