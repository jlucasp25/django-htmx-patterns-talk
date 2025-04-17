var $ltMAx$chartjs = require("chart.js");
var $ltMAx$alpinejs = require("alpinejs");


function $parcel$interopDefault(a) {
  return a && a.__esModule ? a.default : a;
}


(0, $ltMAx$chartjs.Chart).register((0, $ltMAx$chartjs.BarController), (0, $ltMAx$chartjs.BarElement), (0, $ltMAx$chartjs.CategoryScale), (0, $ltMAx$chartjs.LinearScale));
(0, ($parcel$interopDefault($ltMAx$alpinejs))).directive("customer-chart", (el, { expression: expression })=>{
    const config = JSON.parse(expression);
    const chartSettings = {
        scales: {
            x: {
                grid: {
                    display: false
                }
            },
            y: {
                display: false,
                grid: {
                    display: false
                }
            }
        }
    };
    new (0, $ltMAx$chartjs.Chart)(el, {
        type: "bar",
        data: config,
        options: chartSettings
    });
});
(0, ($parcel$interopDefault($ltMAx$alpinejs))).start();


//# sourceMappingURL=index.js.map
