Social = {
	Models: {},
	Views: {},
	Collections: {},
	Routers: {},

	initialize: function () {
		Social.router = new Social.Routers.Router();
		Backbone.history.start()
	}
};

$(document).ready(function () {
	Social.initialize();
})