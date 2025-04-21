import csv

html_header = """<!DOCTYPE html>
<html>
<head>
    <title>Product Blog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        h1 {
            color: #2c3e50;
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }
        .product {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            transition: transform 0.3s;
        }
        .product:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .product img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 5px;
        }
        .product h2 {
            margin-top: 15px;
            color: #2c3e50;
        }
        .price {
            font-weight: bold;
            color: #e74c3c;
            font-size: 1.2em;
            margin: 10px 0;
        }
        footer {
            text-align: center;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <header>
        <h1>Our Product Collection</h1>
        <p>Discover our latest gadgets and tech accessories</p>
    </header>
    <div class="products">"""

html_footer = """</div>
    <footer>
        <p>&copy; 2023 Tech Products Blog</p>
    </footer>
</body>
</html>"""

with open('produk.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    products_html = ""
    
    for row in csv_reader:
        products_html += f"""
        <div class="product">
            <img src="{row['Image']}" alt="{row['Title']}">
            <h2>{row['Title']}</h2>
            <div class="price">{row['Price']}</div>
            <p>{row['Description']}</p>
        </div>"""
    
    full_html = html_header + products_html + html_footer
    
    with open('index.html', 'w') as html_file:
        html_file.write(full_html)
