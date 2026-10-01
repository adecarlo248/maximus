const PRODUCTS = [
  {id:1,name:'Smash Hot',desc:'Garlicky cayenne blast',price:9.99},
  {id:2,name:'Blackout BBQ',desc:'Smoke, molasses, attitude',price:11.99},
  {id:3,name:'Zest Riot',desc:'Citrus + habanero tang',price:10.99},
  {id:4,name:'Midnight Mango',desc:'Sweet heat, tropical kick',price:12.49}
];

const menuEl = document.getElementById('menu');
const cartEl = document.getElementById('cart-items');
const totalEl = document.getElementById('total');
const checkoutBtn = document.getElementById('checkout');
const checkoutModal = document.getElementById('checkout-modal');
const checkoutForm = document.getElementById('checkout-form');
const orderConfirm = document.getElementById('order-confirm');
const orderSummary = document.getElementById('order-summary');

let cart = [];

function renderMenu(){
  menuEl.innerHTML = '';
  PRODUCTS.forEach(p=>{
    const card = document.createElement('div'); card.className='card';
    card.innerHTML = `
      <div class="product-name">${p.name}</div>
      <div class="product-desc">${p.desc}</div>
      <div class="price">$${p.price.toFixed(2)}</div>
      <div class="product-actions">
        <div class="spice">
          <button data-spice="mild">Mild</button>
          <button data-spice="hot">Hot</button>
          <button data-spice="insane">Insane</button>
        </div>
        <input class="qty" type="number" min="1" value="1">
        <button class="btn" data-id="${p.id}">Add</button>
      </div>`;
    menuEl.appendChild(card);
    card.querySelector('[data-id]').addEventListener('click',()=>{
      const qty = Number(card.querySelector('.qty').value)||1;
      const spice = card.querySelector('[data-spice].active')?.dataset.spice || card.querySelector('[data-spice]').dataset.spice;
      addToCart(p,qty,spice);
    });
    card.querySelectorAll('[data-spice]').forEach(b=>b.addEventListener('click',e=>{card.querySelectorAll('[data-spice]').forEach(x=>x.classList.remove('active'));e.target.classList.add('active')}));
  });
}

function addToCart(product, qty=1, spice='mild'){
  const existing = cart.find(i=>i.id===product.id && i.spice===spice);
  if(existing) existing.qty += qty; else cart.push({id:product.id,name:product.name,price:product.price,qty,spice});
  renderCart();
}

function renderCart(){
  if(cart.length===0){cartEl.innerHTML='Empty — add something spicy 🔥'; totalEl.textContent='0.00'; return}
  cartEl.innerHTML='';
  let total=0;
  cart.forEach(item=>{
    const row = document.createElement('div'); row.className='cart-item';
    row.innerHTML = `<div>${item.name} <small style="color:#9aa0a6">×${item.qty} • ${item.spice}</small></div><div>$${(item.price*item.qty).toFixed(2)}</div>`;
    cartEl.appendChild(row);
    total += item.price*item.qty;
  });
  totalEl.textContent = total.toFixed(2);
}

document.getElementById('start-order').addEventListener('click',()=>{document.getElementById('menu').scrollIntoView({behavior:'smooth'})});
document.getElementById('view-order').addEventListener('click',()=>{document.getElementById('cart').scrollIntoView({behavior:'smooth'})});
checkoutBtn.addEventListener('click',()=>{
  if(cart.length===0){alert('Add something first.');return}
  checkoutModal.setAttribute('aria-hidden','false');
});
document.getElementById('close-modal').addEventListener('click',()=>checkoutModal.setAttribute('aria-hidden','true'));

checkoutForm.addEventListener('submit',e=>{
  e.preventDefault();
  const fd = new FormData(checkoutForm); const name=fd.get('name');
  const email=fd.get('email'); const phone=fd.get('phone'); const notes=fd.get('notes');
  const summary = cart.map(i=>`${i.qty}× ${i.name} (${i.spice})`).join('\n');
  orderSummary.textContent = `Thanks ${name}!\nOrder:\n${summary}\nNotes: ${notes || '—'}\nWe will email ${email}${phone?(' • '+phone):''}`;
  checkoutForm.classList.add('hidden'); orderConfirm.classList.remove('hidden');
});

document.getElementById('new-order').addEventListener('click',()=>{
  cart=[]; renderCart(); checkoutForm.reset(); checkoutForm.classList.remove('hidden'); orderConfirm.classList.add('hidden'); checkoutModal.setAttribute('aria-hidden','true');
});

// initial
renderMenu(); renderCart();

