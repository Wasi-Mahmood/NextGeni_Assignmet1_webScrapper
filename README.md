<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>

<h1>NextGeni_Assignmet1_webScrapper</h1>

<p>This Python script utilizes web scraping to compare prices for a specified product on Daraz.pk and iShopping.pk. It provides a comparison of the minimum prices and displays some rows of the dataframes for the cheapest website.</p>

<p>Install the required Python libraries:</p>

<pre><code>pip install beautifulsoup4 pandas selenium
</code></pre>



<pre><code>git clone https://github.com/your-username/your-repo.git
cd your-repo
</code></pre>

<ol start="2">
    <li>Install the necessary Python libraries (as mentioned in the Prerequisites section).</li>
    <li>Run the script:</li>
</ol>

<pre><code>WebScrapper_Asign1.py
</code></pre>

<ol start="4">
    <li>Provide the required inputs:</li>
</ol>

<ul>
    <li>Daraz.pk URL (<code>daraz_url</code>)</li>
    <li>iShopping.pk URL (<code>ishopping_url</code>)</li>
    <li>Keyword for product search (<code>key_word</code>)</li>
</ul>

<h2>Functions</h2>

<h3><code>get_daraz_title_price(url, driver, *args, sleep_time=3)</code></h3>

<p>This function scrapes the title and price information of products from Daraz.pk.</p>

<h3><code>get_ishopping_title_price(url, driver, *args, sleep_time=3)</code></h3>

<p>This function scrapes the title and price information of products from iShopping.pk.</p>

<h3><code>create_df_clean_data(title_list, price_list)</code></h3>

<p>This function creates a clean DataFrame from the title and price lists, removing duplicates and rows with missing or zero values.</p>

<h3><code>get_cheapest_website(url1, url2, key_word, **kwargs)</code></h3>

<p>This main function compares the minimum prices for the given keyword on Daraz.pk and iShopping.pk, and it prints the result along with some rows of the dataframes for the cheapest website.</p>

<h3>Test1.ipynb</h3>

This is a Juypter notebook used for testing purpose. `get_cheapest_website` function is imported from `WebScrapper.py` and run in the notebook for testing purposes.


</body>
</html>
