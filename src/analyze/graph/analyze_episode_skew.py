import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.axes import Axes

from src.analyze.graph.graph_analyzer import GraphAnalyzer
from src.analyze.selector.episode_selector import EpisodeSelector
from src.episode.episode import Episode




class AnalyzeEpisodeSkew(GraphAnalyzer):

    def __init__(self, guru_parent_redraw, matplotlib_canvas :FigureCanvasTkAgg,
                 control_frame :tk.Frame, episode_selector :EpisodeSelector):

        super().__init__(guru_parent_redraw, matplotlib_canvas, control_frame)

        self.episode_selector = episode_selector

    def build_control_frame(self, control_frame):
        episode_selector_frame = self.episode_selector.get_label_frame(control_frame, self.guru_parent_redraw)
        episode_selector_frame.pack()

    def add_plots(self):
        axes :Axes = self.graph_figure.add_subplot()

        # Plot the data

        episode = self.episode_selector.get_selected_episode()
        if not episode:
            return

        plot_x = get_plot_data_steps(episode)

        plot_y_skew = get_plot_data_skew(episode)

        plot_y_track_speeds = get_plot_data_track_speeds(episode)


        axes.plot(plot_x, plot_y_skew, color="C2", label="Skew", linewidth=3)

        # Setup formatting
        axes.set_title("Skew for Episode #" + str(episode.id))
        axes.set_xlabel("Step")
        axes.set_ylabel("Skew (degrees)")
        axes.set_ybound(-20, 20)



def get_plot_data_steps(episode :Episode):

    steps = []

    for v in episode.events:
        steps.append(v.step)

    return np.array(steps)

def get_plot_data_track_speeds(episode :Episode):

    speeds = []

    for v in episode.events:
        speeds.append(v.track_speed)

    return np.array(speeds)

def get_plot_data_skew(episode :Episode):

    skew = []

    for v in episode.events:
        skew.append(v.skew)

    return np.array(skew)