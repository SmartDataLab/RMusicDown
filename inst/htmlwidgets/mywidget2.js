HTMLWidgets.widget({

  name: 'mywidget',

  type: 'output',

  factory: function (el, width, height) {

    // TODO: define shared variables for this instance
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
        console.log('Immediately load inline scripts if no src are provided.')
      } // Immediately load inline scripts if no src are provided.


      if (!srcScripts) {
        onLoad();
        console.log('Load inline scripts once all src scripts are loaded.')
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

    return {

      renderValue: function (x) {

        // TODO: code to render the widget, e.g.
        // el.innerText = x.message;
        // el.innerHTML = x.message;
        // el.innerHTML = '<div class="spinitron-js-widget" data-action="now-playing-v2" data-station="wzbc">demo</div>'
        // TODO put the necessary attribute here
        // if (x === 'NetEaseMusic') {
        el.innerHTML = '<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=450 src="//music.163.com/outchain/player?type=0&id=4886213342&auto=1&height=430"></iframe>'

        // el.setAttribute('class', 'spinitron-js-widget')
        // el.setAttribute('data-action', 'now-playing-v2')
        // el.setAttribute('data-station', 'wzbc')

        // el.setAttribute('data-already-initialized', 'yes');
        // var action = el.getAttribute('data-action');
        // if (['now-playing', 'now-playing-v2', 'upcoming-shows', 'current-playlist'].indexOf(action) < 0) {
        //   action = 'now-playing';
        // }
        // var callback = "_spinitron".concat(1).concat((Math.random().toString() + Date.now()).slice(2, -1));
        // var scriptElement;

        // window[callback] = function (html) {
        //   el.innerHTML = html;
        //   scriptElement.parentElement.removeChild(scriptElement);
        //   delete window[callback];
        //   loadScripts(el);
        // };

        // var query = ['station', 'num', 'count', 'time', 'nolinks', 'sharing', 'player', 'cover', 'merch', 'meta', 'layout', 'image', 'description'].reduce(function (q, param) {
        //   var value = el.getAttribute("data-".concat(param));
        //   return value ? "".concat(q, "&").concat(encodeURIComponent(param), "=").concat(encodeURIComponent(value)) : q;
        // }, "callback=".concat(callback));
        // scriptElement = document.createElement('script');
        // scriptElement.src = "//widgets.spinitron.com/widget/".concat(action, "?").concat(query);
        // // action="now-palying"
        // console.log(scriptElement.src)
        // document.getElementsByTagName('head')[0].appendChild(scriptElement);


      },

      resize: function (width, height) {

        // TODO: code to re-render the widget with a new size

      }

    };
  }
});
