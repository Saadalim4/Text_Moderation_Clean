from app.moderation import moderate_text

def test_safe_text():
    result = moderate_text("I love everyone!", "en", "moderate")
    assert result["classification"].lower() == "safe"

def test_offensive_text():
    result = moderate_text("You are so dumb!", "en", "moderate")
    assert result["classification"].lower() in ["offensive", "harmful", "biased"]