import csv
import os
from datetime import datetime

def generate_html():
    """<!DOCTYPE html>
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

html_footer = """

    with open('index.html', 'w') as html_file:
        html_file.write(full_html)
    
    print("HTML generated successfully!")

def git_commit_push():
    os.system('git add .')
    os.system(f'git commit -m "Auto-update {datetime.now().strftime("%Y-%m-%d %H:%M")}"')
    os.system('git push origin main')
    print("Changes pushed to GitHub!")

if __name__ == "__main__":
    generate_html()
    git_commit_push()
