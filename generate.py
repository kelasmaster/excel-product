import csv

def format_rupiah(amount):
    return f"Rp{amount:,.0f}".replace(",", ".")

def generate_html():
    html_header = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produk Haji & Umroh</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px 0;
            background-color: #2c3e50;
            color: white;
            border-radius: 8px;
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
        }
        .product {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .product:hover {
            transform: translateY(-5px);
        }
        .product img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-bottom: 1px solid #eee;
        }
        .product-info {
            padding: 15px;
        }
        .product h2 {
            margin: 0 0 10px 0;
            color: #2c3e50;
            font-size: 1.2em;
        }
        .price {
            font-weight: bold;
            color: #e74c3c;
            font-size: 1.1em;
            margin: 10px 0;
        }
        .description {
            color: #7f8c8d;
            font-size: 0.9em;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <header>
        <h1>Produk Khusus Haji & Umroh</h1>
        <p>Kebutuhan ibadah Anda yang lebih nyaman dan praktis</p>
    </header>
    <div class="products">"""

    html_footer = """</div>
    <footer>
        <p>&copy; 2024 Toko Produk Haji & Umroh. All rights reserved.</p>
    </footer>
</body>
</html>"""

    products_html = ""
    
    with open('produk.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products_html += f"""
            <div class="product">
                <img src="{row['image']}" alt="{row['title']}">
                <div class="product-info">
                    <h2>{row['title']}</h2>
                    <div class="price">{format_rupiah(int(row['price']))}</div>
                    <p class="description">{row['description']}</p>
                </div>
            </div>"""
    
    full_html = html_header + products_html + html_footer
    
    with open('index.html', 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(full_html)
    print("HTML generated successfully!")

if __name__ == "__main__":
    generate_html()
