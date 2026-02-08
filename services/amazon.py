def search_amazon(query, quick=False):
    return {
        "name": query,
        "platform": "Amazon Now" if quick else "Amazon",
        "price": "99" if quick else "120",
        "link": "amazon://search"
    }
