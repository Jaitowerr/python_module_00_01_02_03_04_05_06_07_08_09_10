def validate_ingredients(ingredients: str, allowed: list[str]) -> str:
    valid = any(i in ingredients.lower() for i in allowed)
    keyword = 'VALID' if valid else 'INVALID'
    return f'{ingredients} - {keyword}'
