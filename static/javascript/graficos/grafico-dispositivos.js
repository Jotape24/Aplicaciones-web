Highcharts.chart('container', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Dispositivos por tipo'
    },
    series: [{
        name: 'Contactos',
        colorByPoint: true,
        data: []
    }]
});

fetch("http://127.0.0.1:5000/get-dispositivos-data")
    .then((response) => response.json())
    .then((data) => {
        let parsedData = data.map((item) => {
            return [item.tipo, item.cantidad_dispositivos];
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