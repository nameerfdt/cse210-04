import random
from casting.artifact import Artifact
from shared.color import Color
from shared.point import Point

COLS = 60
DEFAULT_ARTIFACTS = 3
ARTIFACT_OPTIONS = ["0","*"]

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, cell_size, font_size):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cell_size = cell_size
        self._font_size = font_size
        self._points = 0
        self._updates_loop = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the miner.
        
        Args:
            cast (Cast): The cast of actors.
        """
        miner = cast.get_first_actor("miners")
        velocity = self._keyboard_service.get_direction()
        miner.set_velocity(velocity)

    def _do_updates(self, cast):
        """
        Creates and loops the artifacts.
        Updates the miner's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        miner = cast.get_first_actor("miners")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        miner.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if artifact.get_position().get_y() == max_y+30:
                cast.remove_actor("artifacts", artifact)
            if miner.get_position().equals(artifact.get_position()):
                if artifact.get_text() == "0":
                    self._points += -1
                elif artifact.get_text() == "*":
                    self._points += 1
                message = f"Points: {self._points}"
                banner.set_text(message)
                cast.remove_actor("artifacts", artifact)
        if self._updates_loop % 4 == 0:
            for n in range(DEFAULT_ARTIFACTS):
            
                text = random.choice(ARTIFACT_OPTIONS)

                x = random.randint(1, COLS - 1)
                y = 1
                position = Point(x, y)
                position = position.scale(self._cell_size)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                
                artifact = Artifact()
                artifact.set_velocity(Point(0,5))
                artifact.set_text(text)
                artifact.set_font_size(self._font_size)
                artifact.set_color(color)
                artifact.set_position(position)
                cast.add_actor("artifacts", artifact)
        self._updates_loop +=1

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()