hqDefine("app_manager/js/app_exchange", [
    "jquery",
    "knockout",
    "hqwebapp/js/widgets",  // hqwebapp-select2 for versions
], function (
    $,
    ko
) {
    var AppExchangeModel = function () {
        var self = {};

        self.showVersions = ko.observable(false);

        self.versionButtonText = ko.computed(function () {
            if (self.showVersions()) {
                return gettext("Hide Version History");
            }
            return gettext("Show Version History");
        });

        self.toggleVersions = function () {
            self.showVersions(!self.showVersions());
        };

        return self;
    };

    $(function () {
        $("#hq-content").koApplyBindings(AppExchangeModel());
    });
});
