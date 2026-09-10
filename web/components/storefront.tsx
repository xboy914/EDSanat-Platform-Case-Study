"use client";
import {useEffect,useMemo,useState} from "react";
import {catalogue,checkout,Product} from "../lib/api";

type Cart=Record<number,number>;

export function Storefront(){
 const[products,setProducts]=useState<Product[]>([]);
 const[cart,setCart]=useState<Cart>({});
 const[token,setToken]=useState("");
 const[state,setState]=useState("Loading synthetic catalogue…");
 useEffect(()=>{catalogue().then(data=>{setProducts(data);setState(data.length?"":"No demo products yet.")}).catch(error=>setState(error.message))},[]);
 const count=Object.values(cart).reduce((sum,value)=>sum+value,0);
 const total=useMemo(()=>products.reduce((sum,p)=>sum+Number(p.price)*(cart[p.id]??0),0),[products,cart]);
 function add(product:Product){setCart(current=>({...current,[product.id]:Math.min((current[product.id]??0)+1,product.stock)}))}
 async function submit(){if(!token){setState("Paste a demo JWT access token first.");return}try{const order=await checkout(token,Object.entries(cart).map(([id,quantity])=>({product_id:Number(id),quantity})));setCart({});setState(`Order #${order.id} placed · ${order.total}`)}catch(error){setState(error instanceof Error?error.message:"Checkout failed")}}
 return <><header><span>FULL-STACK COMMERCE / CLEAN-ROOM DEMO</span><h1>Industrial tools.<br/><em>One connected stack.</em></h1><p>Next.js storefront backed by server-authoritative Django checkout. Every product and value shown here is synthetic.</p></header>
 <div className="toolbar"><input aria-label="JWT access token" type="password" value={token} onChange={e=>setToken(e.target.value)} placeholder="Demo JWT access token"/><div><strong>{count}</strong> items · <strong>{total.toFixed(2)}</strong><button disabled={!count} onClick={submit}>Secure checkout</button></div></div>
 {state&&<p className="status">{state}</p>}
 <section className="products">{products.map(product=><article key={product.id}><div className="image">{product.images[0]?<img src={product.images[0].url} alt={product.images[0].alt_text}/>:<span>NO SYNTHETIC IMAGE</span>}</div><small>{product.category_name} / {product.sku}</small><h2>{product.name}</h2><div className="price"><b>{product.price}</b><span>{product.stock} available</span></div><button disabled={!product.stock} onClick={()=>add(product)}>Add to cart</button></article>)}</section>
 <footer>Public case study · No production EDSanat source or customer data</footer></>
}
