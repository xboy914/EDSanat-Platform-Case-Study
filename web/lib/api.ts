export type ProductImage={url:string;alt_text:string;position:number};
export type Product={id:number;sku:string;name:string;category_name:string;price:string;stock:number;images:ProductImage[]};
export type Order={id:number;status:string;total:string;lines:{sku:string;product_name:string;unit_price:string;quantity:number;line_total:string}[]};

const API=process.env.NEXT_PUBLIC_API_URL??"http://localhost:8000";

async function request<T>(path:string,init?:RequestInit):Promise<T>{
 const response=await fetch(`${API}${path}`,init);
 if(!response.ok){const payload=await response.json().catch(()=>({detail:"Request failed"}));throw new Error(payload.detail??`HTTP ${response.status}`)}
 return response.json() as Promise<T>;
}

export const catalogue=()=>request<Product[]>("/api/products/");
export const checkout=(token:string,lines:{product_id:number;quantity:number}[])=>request<Order>("/api/orders/checkout/",{
 method:"POST",
 headers:{"Content-Type":"application/json",Authorization:`Bearer ${token}`},
 body:JSON.stringify({idempotency_key:crypto.randomUUID(),lines})
});
