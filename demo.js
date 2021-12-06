"use strict";

(function () {
    Array.from(document.querySelectorAll('.spinitron-js-widget')).forEach(function (widget, index) {
        if (widget.getAttribute('data-already-initialized') === 'yes') {
            return;
        }

        widget.setAttribute('data-already-initialized', 'yes');
        var action = widget.getAttribute('data-action');

        if (['now-playing', 'now-playing-v2', 'upcoming-shows', 'current-playlist'].indexOf(action) < 0) {
            action = 'now-playing';
        }

        var callback = "_spinitron".concat(index).concat((Math.random().toString() + Date.now()).slice(2, -1));
        var scriptElement;

        window[callback] = function (html) {
            widget.innerHTML = html;
            scriptElement.parentElement.removeChild(scriptElement);
            delete window[callback];
            loadScripts(widget);
        };

        var query = ['station', 'num', 'count', 'time', 'nolinks', 'sharing', 'player', 'cover', 'merch', 'meta', 'layout', 'image', 'description'].reduce(function (q, param) {
            var value = widget.getAttribute("data-".concat(param));
            return value ? "".concat(q, "&").concat(encodeURIComponent(param), "=").concat(encodeURIComponent(value)) : q;
        }, "callback=".concat(callback));
        scriptElement = document.createElement('script');
        scriptElement.src = "//widgets.spinitron.com/widget/".concat(action, "?").concat(query);
        document.getElementsByTagName('head')[0].appendChild(scriptElement);
    });

    function loadScripts(widget) {
        var head = document.getElementsByTagName('head')[0];
        var srcScripts = 0;
        var inlineSripts = []; // Count src scripts.

        var scripts = Array.prototype.slice.call(widget.getElementsByTagName('script'));

        for (var i = 0; i < scripts.length; i += 1) {
            if (scripts[i].src) {
                srcScripts += 1;
            }
        } // Create <script> tags, load src tags, schedule inline tags.


        for (var _i = 0; _i < scripts.length; _i += 1) {
            var script = document.createElement('script');

            if (scripts[_i].src) {
                script.src = scripts[_i].src;
                script.onload = onLoad;
                script.async = false;
                head.appendChild(script);
                head.removeChild(script);
            } else {
                script.innerHTML = scripts[_i].innerHTML;
                inlineSripts.push(script);
            }
        } // Immediately load inline scripts if no src are provided.


        if (!srcScripts) {
            onLoad();
        } // Load inline scripts once all src scripts are loaded.


        function onLoad() {
            srcScripts -= 1;

            if (!srcScripts) {
                for (var _i2 = 0; _i2 < inlineSripts.length; _i2++) {
                    head.appendChild(inlineSripts[_i2]);
                    head.removeChild(inlineSripts[_i2]);
                }
            }
        }
    }
})();