import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.gridspec import GridSpec
from matplotlib.axes import Axes

from src.analyze.graph.graph_analyzer import GraphAnalyzer
from src.utils.lists import get_list_of_empty_lists


ROUNDING_EXACT = "Exact"
ROUNDING_INTEGER = "Integer"

class AnalyzeCommonRewards(GraphAnalyzer):

    def __init__(self, guru_parent_redraw, matplotlib_canvas :FigureCanvasTkAgg, control_frame :tk.Frame):

        super().__init__(guru_parent_redraw, matplotlib_canvas, control_frame)

        self.rounding = tk.StringVar()
        self.rounding.set(ROUNDING_EXACT)


    def build_control_frame(self, control_frame):
        rounding_group = tk.LabelFrame(control_frame, text="Rounding", padx=5, pady=5)
        rounding_group.pack()

        tk.Radiobutton(rounding_group, text=ROUNDING_EXACT, variable=self.rounding, value=ROUNDING_EXACT,
                       command=self.guru_parent_redraw).grid(column=0, row=0, pady=2, padx=5)
        tk.Radiobutton(rounding_group, text=ROUNDING_INTEGER, variable=self.rounding, value=ROUNDING_INTEGER,
                       command=self.guru_parent_redraw).grid(column=0, row=1, pady=2, padx=5)


    def add_plots(self):
        if not self.all_episodes:
            return

        gs = GridSpec(1, 2)
        axes_left :Axes = self.graph_figure.add_subplot(gs[0, 0])
        axes_right :Axes = self.graph_figure.add_subplot(gs[0, 1])

        self.plot_common_rewards(axes_left, self.all_episodes, "All", "C1")
        self.plot_common_rewards(axes_right, self.filtered_episodes, "Filtered", "C2")


    def plot_common_rewards(self, axes :Axes, episodes, label, colour):
        # Plot data

        round_to_integer = self.rounding.get() == ROUNDING_INTEGER

        if episodes:
            add_plot_for_common_rewards(axes, episodes, colour, round_to_integer)

        # Format the plot
        axes.set_title("Most Frequent Reward Per Step\n(" + label + " Episodes)")
        axes.set_xlabel("Count")


def get_plot_data_for_common_rewards(episodes, round_to_integer):

    all_step_rewards = []

    for e in episodes:
        for v in e.events:
            if round_to_integer:
                all_step_rewards.append(round(v.reward))
            else:
                all_step_rewards.append(v.reward)

    unique_rewards, unique_counts = np.unique(np.array(all_step_rewards), return_counts=True)

    plot_rewards = []
    plot_counts = []

    for i in range(0, 10):
        index = np.argmax(unique_counts)

        plot_rewards.append(unique_rewards[index])
        plot_counts.append(unique_counts[index])

        unique_counts[index] = 0

    return plot_rewards, plot_counts

def add_plot_for_common_rewards(axes :Axes, episodes, colour, round_to_integer):
    (plot_rewards, plot_counts) = get_plot_data_for_common_rewards(episodes, round_to_integer)

    y_pos = np.arange(len(plot_counts))

    axes.barh(y_pos, plot_counts, color=colour)
    axes.set_yticks(y_pos)
    axes.set_yticklabels(plot_rewards)
