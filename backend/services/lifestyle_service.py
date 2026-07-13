class LifestyleService:

    def __init__(self):

        self.recommendations = {

            "Normal": {

                "about": (
                    "Your eyes appear healthy based on the AI prediction. "
                    "Maintain healthy habits and schedule regular eye check-ups "
                    "to protect your vision."
                ),

                "diet": [
                    "Eat green leafy vegetables like spinach and broccoli.",
                    "Include fresh fruits rich in Vitamin C.",
                    "Drink 2-3 liters of water daily.",
                    "Eat nuts and seeds for healthy fats."
                ],

                "exercise": [
                    "Walk for at least 30 minutes daily.",
                    "Practice the 20-20-20 eye rule while using screens.",
                    "Sleep for 7-8 hours every night."
                ],

                "eye_care": [
                    "Get an eye examination once every year.",
                    "Wear sunglasses when going outside.",
                    "Take breaks during long screen usage."
                ],

                "avoid": [
                    "Smoking",
                    "Excessive screen time",
                    "Poor sleep habits"
                ]
            },

            "Cataract": {

                "about": (
                    "Cataract makes the natural lens of the eye cloudy, "
                    "causing blurry or dim vision. Early treatment helps "
                    "prevent further vision problems."
                ),

                "diet": [
                    "Eat carrots, spinach and kale.",
                    "Consume Vitamin C rich fruits.",
                    "Eat foods containing antioxidants.",
                    "Drink enough water."
                ],

                "exercise": [
                    "Daily walking.",
                    "Light stretching exercises.",
                    "Maintain a healthy body weight."
                ],

                "eye_care": [
                    "Wear UV-protective sunglasses.",
                    "Visit an ophthalmologist regularly.",
                    "Protect your eyes from dust."
                ],

                "avoid": [
                    "Smoking",
                    "Too much sunlight",
                    "Alcohol",
                    "Skipping eye check-ups"
                ]
            },

            "Glaucoma": {

                "about": (
                    "Glaucoma increases pressure inside the eye and may damage "
                    "the optic nerve. Early detection helps prevent permanent "
                    "vision loss."
                ),

                "diet": [
                    "Eat green leafy vegetables.",
                    "Include fish rich in Omega-3.",
                    "Drink enough water throughout the day.",
                    "Eat fruits rich in antioxidants."
                ],

                "exercise": [
                    "Walk for 30 minutes daily.",
                    "Practice light aerobic exercise.",
                    "Reduce stress through relaxation exercises."
                ],

                "eye_care": [
                    "Use prescribed eye drops regularly.",
                    "Monitor eye pressure.",
                    "Attend regular eye check-ups."
                ],

                "avoid": [
                    "Smoking",
                    "Skipping medication",
                    "Too much caffeine",
                    "Long continuous screen usage"
                ]
            },

            "AMD": {

                "about": (
                    "Age-related Macular Degeneration affects the central part "
                    "of the retina and can reduce sharp central vision."
                ),

                "diet": [
                    "Eat spinach and kale.",
                    "Eat fish rich in Omega-3.",
                    "Consume nuts and seeds.",
                    "Eat colorful fruits and vegetables."
                ],

                "exercise": [
                    "Daily walking.",
                    "Maintain healthy body weight.",
                    "Stay physically active."
                ],

                "eye_care": [
                    "Regular retinal examination.",
                    "Wear sunglasses outdoors.",
                    "Monitor any vision changes immediately."
                ],

                "avoid": [
                    "Smoking",
                    "High-fat foods",
                    "Ignoring vision changes"
                ]
            }

        }

    def get_recommendations(self, disease):

        return self.recommendations.get(
            disease,
            {
                "about": "No recommendation available.",
                "diet": [],
                "exercise": [],
                "eye_care": [],
                "avoid": []
            }
        )