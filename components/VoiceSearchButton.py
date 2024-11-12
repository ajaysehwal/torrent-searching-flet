import flet as ft
from flet import *
import asyncio

class VoiceSearch(UserControl):
    def __init__(self, on_result):
        super().__init__()
        self.on_result = on_result
        self.is_listening = False
        
    def build(self):
        # Create the voice visualization circles
        self.circles = [
            Container(
                width=6,
                height=6,
                border_radius=3,
                bgcolor=colors.BLUE_400,
                visible=False,
                animate=animation.Animation(150, AnimationCurve.EASE_IN_OUT),
            ) for _ in range(3)
        ]
        
        # Create the microphone button
        self.mic_button = IconButton(
            icon=icons.MIC,
            icon_color=colors.BLACK,
            tooltip="Voice Search",
            on_click=self.toggle_voice_search
        )
        
        return Container(
            content=Column(
                controls=[
                    # Microphone button with animation circles
                    Stack(
                        controls=[
                            Row(
                                controls=self.circles,
                                alignment=MainAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            self.mic_button,
                        ],
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=4
            ),
            width=40,
            height=50
        )

    def animate_listening(self):
        """Create a simple wave animation for the circles"""
        heights = [15, 8, 12]  # Different heights for each circle
        
        async def animate():
            while self.is_listening:
                for i, circle in enumerate(self.circles):
                    circle.height = heights[i]
                    circle.update()
                await asyncio.sleep(0.2)
                
                for circle in self.circles:
                    circle.height = 6
                    circle.update()
                await asyncio.sleep(0.2)
                
                heights.append(heights.pop(0))  # Rotate heights for next animation
        
        asyncio.create_task(animate())

    def start_listening(self):
        """Start the voice recognition"""
        self.is_listening = True
        self.mic_button.icon_color = colors.RED_400
        
        # Show and start animating the circles
        for circle in self.circles:
            circle.visible = True
        
        # Start the animation
        self.animate_listening()
        
        # Start speech recognition using page's JavaScript
        self.page.launch_url("javascript:void((function() { \
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)(); \
            recognition.lang = 'en-US'; \
            recognition.interimResults = false; \
            recognition.maxAlternatives = 1; \
            recognition.onresult = (event) => { \
                const transcript = event.results[0][0].transcript; \
                window.pywebview.api.handle_speech_result(transcript); \
            }; \
            recognition.onerror = (event) => { \
                window.pywebview.api.handle_speech_error(event.error); \
            }; \
            recognition.onend = () => { \
                window.pywebview.api.stop_listening(); \
            }; \
            recognition.start(); \
        })())")
        
        self.update()

    def stop_listening(self):
        """Stop the voice recognition"""
        if self.is_listening:
            self.is_listening = False
            self.mic_button.icon_color = colors.BLACK
            
            # Hide the circles
            for circle in self.circles:
                circle.visible = False
            
            self.update()

    def toggle_voice_search(self, e):
        """Toggle voice search on/off"""
        if not self.is_listening:
            self.start_listening()
        else:
            self.stop_listening()

    async def handle_speech_result(self, text):
        """Handle the speech recognition result"""
        self.stop_listening()
        if text:
            await self.on_result(text)

    def handle_speech_error(self, error):
        """Handle any speech recognition errors"""
        self.stop_listening()
        self.page.show_snack_bar(
            SnackBar(
                content=Text("Could not understand audio. Please try again."),
                action="OK"
            )
        )