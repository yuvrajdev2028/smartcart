import { Badge } from "@/components/ui/badge";

export default function ProductCard({ product }) {
  return (
    <div className="group rounded-xl border border-border/50 bg-card/40 overflow-hidden hover:border-primary/30 hover:bg-card/70 transition-all duration-300">
      <div className="aspect-[4/5] overflow-hidden bg-muted/30">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          loading="lazy"
        />
      </div>
      <div className="p-4">
        <div className="flex items-start justify-between gap-2 mb-1">
          <h3 className="font-medium text-sm leading-tight">{product.name}</h3>
          <span className="text-sm font-semibold text-primary shrink-0">
            ${product.price}
          </span>
        </div>
        <p className="text-xs text-muted-foreground mb-3 line-clamp-2">
          {product.description}
        </p>
        <div className="flex items-center gap-1.5 flex-wrap">
          <Badge variant="secondary" className="text-[10px] px-1.5 py-0">
            {product.brand}
          </Badge>
          <Badge variant="outline" className="text-[10px] px-1.5 py-0">
            {product.color}
          </Badge>
        </div>
      </div>
    </div>
  );
}
