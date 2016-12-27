/* globals hqDefine moment alert_user */
hqDefine('userreports/js/expression_evaluator.js', function () {
    var ExpressionModel = function (editor, submitUrl) {
        var self = this;
        self.editor = editor;
        self.submitUrl = submitUrl;
        self.documentType = ko.observable();
        self.documentId = ko.observable();
        self.expressionText = ko.observable(editor.getValue());
        self.uiFeedback = ko.observable();

        self.getExpressionJSON = function () {
            try {
                return JSON.parse(self.expressionText());
            } catch (err) {
                return null;
            }
        };
        self.editor.on('change', function () {
            self.expressionText(self.editor.getValue());
        });

        self.hasError = ko.computed(function () {
            return self.getExpressionJSON() === null;
        }, self);

        self.evaluateExpression = function(formElement) {
            self.uiFeedback("");
            if (self.hasError()) {
                self.uiFeedback("Please fix all parsing errors before evaluating.")
            } else if (!self.documentId()) {
                self.uiFeedback("Please enter a document ID.")
            }
            else {
                $.post({
                    url: self.submitUrl,
                    data: {
                        doc_type: self.documentType(),
                        doc_id: self.documentId(),
                        expression: self.expressionText(),
                    },
                    success: function (data) {
                        self.uiFeedback("<strong>Result:</strong> " + data.result);
                    },
                    error: function (data) {
                        self.uiFeedback("<strong>Failure!:</strong> " + data.responseJSON.error);
                    },
                });
            }
        };
    };
    return {ExpressionModel: ExpressionModel};
});
