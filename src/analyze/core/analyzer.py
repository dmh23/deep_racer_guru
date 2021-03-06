import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from src.log.log_meta import LogMeta
from matplotlib import style as mpl_style



class Analyzer:

    def __init__(self, guru_parent_redraw, control_frame :tk.Frame):
        self.guru_parent_redraw = guru_parent_redraw
        self.control_frame = control_frame

        self.current_track = None
        self.filtered_episodes = None
        self.all_episodes = None
        self.action_space = None
        self.action_space_filter = None
        self.log_meta = None
        self.evaluation_phases = None


    def take_control(self):

        for widget in self.control_frame.winfo_children():
            widget.destroy()

        self.build_control_frame(self.control_frame)

        tk.Label(self.control_frame, text="                                                 ").pack()

        self.control_frame.pack(side=tk.RIGHT)

    def set_track(self, current_track):
        self.current_track = current_track
        self.warning_track_changed()

    def set_all_episodes(self, all_episodes):
        self.all_episodes = all_episodes
        self.warning_all_episodes_changed()

    def set_log_meta(self, log_meta :LogMeta):
        self.log_meta = log_meta

    def set_evaluation_phases(self, evaluation_phases):
        self.evaluation_phases = evaluation_phases

    def set_filtered_episodes(self, filtered_episodes):
        self.filtered_episodes = filtered_episodes
        self.warning_filtered_episodes_changed()

    def set_action_space(self, action_space):
        self.action_space = action_space
        self.warning_action_space_changed()

    def set_action_space_filter(self, action_space_filter):
        self.action_space_filter = action_space_filter
        self.warning_action_space_filter_changed()


    ##########################
    ### ABSTRACT INTERFACE ###
    ##########################

    def uses_graph_canvas(self):
        # You *MUST* override this
        pass

    def uses_track_graphics(self):
        # You *MUST* override this
        pass

    def redraw(self):
        # You *MUST* override this
        pass

    def build_control_frame(self, control_frame):
        # You *MUST* override this
        pass

    def recalculate(self):
        # You MIGHT override this to perform time-consuming analysis before redrawing
        pass

    def warning_track_changed(self):
        # You MIGHT override this to manage cached or pre-calculated data structures
        # Do not override to redraw() since Guru already calls redraw() at the right times!
        pass

    def warning_filtered_episodes_changed(self):
        # You MIGHT override this to manage cached or pre-calculated data structures
        # Do not override to redraw() since Guru already calls redraw() at the right times!
        pass

    def warning_all_episodes_changed(self):
        # You MIGHT override this to manage cached or pre-calculated data structures
        # Do not override to redraw() since Guru already calls redraw() at the right times!
        pass

    def warning_action_space_changed(self):
        # You MIGHT override this to manage cached or pre-calculated data structures
        # Do not override to redraw() since Guru already calls redraw() at the right times!
        pass

    def warning_action_space_filter_changed(self):
        # You MIGHT override this to manage cached or pre-calculated data structures
        # Do not override to redraw() since Guru already calls redraw() at the right times!
        pass

