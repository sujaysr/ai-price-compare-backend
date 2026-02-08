def search_flipkart(query, quick=False):
    return {
        "name": query,
        "platform": "Flipkart Minutes" if quick else "Flipkart",
        "price": "95" if quick else "115",
        "link": "flipkart://search"
    }
