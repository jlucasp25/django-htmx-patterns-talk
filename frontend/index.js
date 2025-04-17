import {
  Chart,
  BarController,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import Alpine from "alpinejs";
Chart.register(
  BarController,
  BarElement,
  CategoryScale,
  LinearScale
);

Alpine.directive("customer-chart", (el, {expression}) => {
    const config = JSON.parse(expression);

    const chartSettings = {
        scales: {
            x: {
                grid: {
                    display: false,
                }
            },
            y: {
                display: false,
                grid: {display: false}
            },
        },
    };

    new Chart(el, {
        type: "bar",
        data: config,
        options: chartSettings
    });
});

Alpine.start();
