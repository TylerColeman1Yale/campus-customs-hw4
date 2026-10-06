import json, sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / 'data' / 'campus_customs.db'

def connect():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def product_from_row(row, conn):
    p = dict(row)
    stock = {r['size']: r['quantity'] for r in conn.execute('select size, quantity from inventory where product_id=?', (p['product_id'],))}
    p['inventory'] = stock
    return p

def list_products(query=''):
    conn = connect(); q = f'%{query.lower()}%'
    rows = conn.execute('select * from catalogue where lower(name||" "||garment_type||" "||description||" "||search_tags) like ? order by name limit 12', (q,)).fetchall() if query else conn.execute('select * from catalogue order by name limit 12').fetchall()
    result = [product_from_row(r, conn) for r in rows]; conn.close(); return result

def get_product(product_id):
    conn = connect(); row = conn.execute('select * from catalogue where product_id=?', (product_id,)).fetchone()
    result = product_from_row(row, conn) if row else None; conn.close(); return result

def find_answer(message, product_id=None):
    terms = message.lower()
    category = next((x for x in ('hoodie','crewneck','shirt','sweater','jacket','zip') if x in terms), None)
    products = list_products(category) if category else []
    if product_id and not products: products = [get_product(product_id)]
    products = [p for p in products if p]
    if products:
        p = products[0]
        if 'price' in terms or '$' in terms: return f"{p['name']} is ${p['price']:.2f}.", products
        words = set(terms.replace('?', ' ').replace(',', ' ').split())
        size = next((s.upper() for s in p['inventory'] if s.lower() in words), None)
        if 'stock' in terms or 'available' in terms or size:
            if size: return f"{p['name']} has {p['inventory'].get(size, 0)} in stock in size {size}.", products
            total = sum(p['inventory'].values()); return f"{p['name']} has {total} total units across its listed sizes.", products
        return f"I found {len(products)} Campus Customs match{'es' if len(products)!=1 else ''}. Here are some options.", products
    return "I can help with Yale merchandise, prices, and real inventory. What product or category should I check?", []
