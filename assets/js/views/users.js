Social.Views.Users = Backbone.View.extend({
	template: _.template(JFT['users']),
	render: function () {
		this.$el.html(this.template({
			users: this.collection
		}))
	}
})