Social = {
	Models: {},
	Views: {},
	Collections: {},
	Routers: {},

	initialize = function () {
		Social.router = new Socail.Routers.Router();
		Backbone.history.start()
	}
};

$(document).ready(function () {
	Social.initialize();
})