Highcharts.chart('container', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Contactos por Comuna'
    },
    series: [{
        name: 'Contactos',
        colorByPoint: true,
        data: []
    }]
});


fetch("http://127.0.0.1:5000/get-contactos-data")
    .then((response) => response.json())
    .then((data) => {
        let parsedData = data.map((item) => {
            return [item.comuna, item.cantidad_contactos];
        });

        const chart = Highcharts.charts.find(
            (chart) => chart && chart.renderTo.id === "container"
        );

        chart.update({
            series: [
                {
                data: parsedData,
                },
            ],
        });
    })
    .catch((error) => console.error("Error:", error));