Social.Routers.Router = Backbone.Router.extend({
	routes: {
		users: 'users'
	},

	initialize: function () {
		this.$app = $('#app');
	},

	users: function () {
		var collection = new Social.Collections.Users(),
			self = this;

		collection.fetch({
			success: function () {
				var view = new Social.Views.Users({
					collection: collection
				});
				self._swapView(view);
			},
			error: function () {alert('error')}
		})
	},

	_swapView : function (view) {
		if (this.currentView) this.currentView.remove();
		this.currentView = view;
		this.$app.html(view.$el);
		view.render();
	},
});