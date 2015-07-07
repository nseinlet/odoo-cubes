openerp.biwizard = function(instance, local) {

    local.biwiz = instance.web.PivotView.extend({

        init: function (model, domain, fields, options) {
    		this.cells = [];
    		this.domain = domain;
            this.context = options.context;
    		this.no_data = true;
    		this.updating = false;
    		this.model = model;
    		this.fields = fields;
            this.measures = [];
            this.rows = { groupby: options.row_groupby, headers: null };
            this.cols = { groupby: options.col_groupby, headers: null };
            console.log("bi wizard loaded");
        },
    });

}
