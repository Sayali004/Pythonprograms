import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Diet Recommendation Expert System",
    page_icon="🍎",
    layout="wide"
)

# -------------------------------
# Custom CSS Styling
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .header {
        background-color: #2E8B57;
        padding: 1.5rem;
        text-align: center;
        color: white;
        border-radius: 10px;
    }
    .result-box {
        background-color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        color: #666;
        margin-top: 30px;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Header Section
# -------------------------------
st.markdown("<div class='header'><h1>🍎 Diet Recommendation Expert System</h1><p>Your Smart Personal Nutrition Guide</p></div>", unsafe_allow_html=True)
st.write("")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("🔍 Enter Your Details")

age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
activity = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])
goal = st.sidebar.selectbox("Fitness Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])
diet_preference = st.sidebar.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
current_weight = st.sidebar.number_input("Current Weight (kg)", min_value=30, max_value=200, value=60)
target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=30, max_value=200, value=55)
st.sidebar.markdown("---")
st.sidebar.info("💡 Click the button below to generate your personalized diet plan.")

# -------------------------------
# Expert System Function
# -------------------------------
def recommend_diet(age, gender, activity, goal, current_weight, target_weight, diet_preference):
    # Base calorie setup
    if gender == "Male":
        base_calories = 2500
    else:
        base_calories = 2000

    if activity == "Low":
        base_calories -= 300
    elif activity == "High":
        base_calories += 300

    # Adjust for goal
    if goal == "Weight Loss":
        calories = base_calories - 500
        diet_type = "Low-carb, high-protein diet with more vegetables and fiber."
    elif goal == "Weight Gain":
        calories = base_calories + 500
        diet_type = "High-protein, calorie-dense meals with frequent snacks."
    else:
        calories = base_calories
        diet_type = "Balanced diet with moderate carbs, fats, and proteins."

    # Weight difference message
    weight_diff = target_weight - current_weight
    if weight_diff < 0:
        progress = f"You aim to lose **{abs(weight_diff)} kg**. Stay consistent with controlled calories and exercise."
    elif weight_diff > 0:
        progress = f"You aim to gain **{weight_diff} kg**. Add extra protein and calorie-dense foods."
    else:
        progress = "Your target weight is the same as your current weight — focus on maintaining balance."

    # Daily Meal Plan based on diet preference
    if diet_preference == "Vegetarian":
        if goal == "Weight Loss":
            meals = [
                "🥣 Breakfast: Oats with fruits and green tea",
                "🥗 Lunch: Grilled paneer with vegetables",
                "🍲 Dinner: Lentil soup and salad"
            ]
        elif goal == "Weight Gain":
            meals = [
                "🍳 Breakfast: Milk, banana, and peanut butter toast",
                "🍛 Lunch: Rice, dal, paneer curry, and yogurt",
                "🥘 Dinner: Roti with sabzi and milkshake"
            ]
        else:
            meals = [
                "🍞 Breakfast: Whole grains with milk and fruits",
                "🍚 Lunch: Rice, dal, sabzi, and salad",
                "🍜 Dinner: Light meal with soup and chapati"
            ]

    elif diet_preference == "Non-Vegetarian":
        if goal == "Weight Loss":
            meals = [
                "🥣 Breakfast: Egg whites with toast and green tea",
                "🥗 Lunch: Grilled chicken with veggies",
                "🍲 Dinner: Soup and boiled eggs"
            ]
        elif goal == "Weight Gain":
            meals = [
                "🍳 Breakfast: Eggs, milk, and peanut butter toast",
                "🍛 Lunch: Rice, chicken curry, and yogurt",
                "🥘 Dinner: Fish curry with rice and milkshake"
            ]
        else:
            meals = [
                "🍞 Breakfast: Eggs and whole grains with fruits",
                "🍚 Lunch: Balanced meal with rice, dal, and grilled chicken",
                "🍜 Dinner: Soup and chapati with omelette"
            ]

    else:  # Vegan
        if goal == "Weight Loss":
            meals = [
                "🥣 Breakfast: Oats with almond milk and fruits",
                "🥗 Lunch: Quinoa salad with tofu",
                "🍲 Dinner: Lentil soup and stir-fried veggies"
            ]
        elif goal == "Weight Gain":
            meals = [
                "🍳 Breakfast: Smoothie with oats, banana, and soy milk",
                "🍛 Lunch: Rice, beans, and tofu curry",
                "🥘 Dinner: Vegan burrito and almond milkshake"
            ]
        else:
            meals = [
                "🍞 Breakfast: Peanut butter toast with almond milk",
                "🍚 Lunch: Brown rice, lentils, and veggies",
                "🍜 Dinner: Soup and tofu stir fry"
            ]

    # Weekly Meal Schedule
    weekly_plan = {
        "Monday": "Oats, rice bowl with protein source, salad",
        "Tuesday": "Smoothie, grilled protein meal, soup",
        "Wednesday": "Upma, lentils, and veggies",
        "Thursday": "Fruit smoothie, chapati with protein, and salad",
        "Friday": "Poha, protein rice bowl, and soup",
        "Saturday": "Sandwich, rice with dal, and steamed veggies",
        "Sunday": "Cheat day! Enjoy one favorite meal moderately 🍕"
    }

    # Health tips
    tips = [
        "💧 Stay hydrated — drink 2–3 liters of water daily.",
        "🥦 Include seasonal vegetables and fruits.",
        "⏰ Eat every 3–4 hours to maintain energy.",
        "🚶 Exercise or walk at least 30 minutes daily."
    ]

    return calories, diet_type, meals, tips, progress, weekly_plan


# -------------------------------
# Recommendation Output
# -------------------------------
if st.sidebar.button("💬 Generate Diet Plan"):
    calories, diet_type, meals, tips, progress, weekly_plan = recommend_diet(
        age, gender, activity, goal, current_weight, target_weight, diet_preference
    )

    st.markdown("## 🧠 Personalized Diet Recommendation")

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("📊 Recommended Daily Calories")
    st.write(f"**{calories} kcal**")
    st.subheader("🥗 Diet Type")
    st.write(diet_type)
    st.subheader("⚖️ Weight Goal Summary")
    st.write(progress)
    st.subheader("🍀 Diet Preference")
    st.write(f"You chose a **{diet_preference}** plan.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("🍽️ Sample Meal Plan")
    for meal in meals:
        st.write(f"- {meal}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("📅 Weekly Meal Schedule")
    for day, plan in weekly_plan.items():
        st.write(f"**{day}:** {plan}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("💡 Nutrition & Lifestyle Tips")
    for tip in tips:
        st.write(f"- {tip}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.balloons()

else:
    st.warning("⬅️ Please fill in your details in the sidebar and click *Generate Diet Plan* to view your results.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("<div class='footer'>Developed by Sayali Dabade | Powered by Streamlit</div>", unsafe_allow_html=True)

#streamlit run diet_expert_system.py