class ViewBus:
    def execute(self, view):
        self.parent.active_view_name = view


viewbus = ViewBus()
