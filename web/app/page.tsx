const layers=[
 ["BACKEND","Django · DRF · PostgreSQL","Versioned APIs, business rules and auditability."],
 ["WEB","Next.js · TypeScript","Responsive commerce and operations workspace."],
 ["ANDROID","Flutter · Dart","Mobile catalogue and field operations experience."],
 ["WINDOWS","WinUI 3 · .NET 8","Offline-first administration and point of sale."]
];
export default function Home(){return <main><header><span>FULL-STACK CASE STUDY</span><h1>One platform.<br/><em>Four clients.</em></h1><p>A privacy-safe reconstruction demonstrating the architecture and engineering decisions behind a multi-channel industrial commerce platform.</p></header><section>{layers.map(([name,stack,copy],i)=><article key={name}><small>0{i+1} / {name}</small><h2>{stack}</h2><p>{copy}</p></article>)}</section><footer>100% synthetic demo data · No production source disclosed</footer></main>}
