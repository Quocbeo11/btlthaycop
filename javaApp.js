// Hàm để tải dữ liệu từ URL JSON và vẽ biểu đồ nhiệt độ và độ ẩm
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);
function drawCharts() {
    drawTemperatureChart();
    drawHumidityChart();
}
function loadData(url, callback) {
    fetch(url)
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.error('Error loading data:', error));
}

// Hàm để vẽ biểu đồ nhiệt độ
function drawTemperatureChart() {
    loadData('http://127.0.0.1:1880/get-temp', function(data) {
        var chartData = [];
        chartData.push(['Date', 'Temperature']);

        data.forEach(function(entry) {
            chartData.push([new Date(entry.Date), entry.Temperature]);
        });

        var dataTable = google.visualization.arrayToDataTable(chartData);

        var options = {
            title: 'Temperature Chart',
            curveType: 'function',
            legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('temperature_chart'));
        chart.draw(dataTable, options);
    });
}

// Hàm để vẽ biểu đồ độ ẩm
function drawHumidityChart() {
    loadData('http://127.0.0.1:1880/get-humi', function(data) {
        var chartData = [];
        chartData.push(['Time', 'Humidity']);

        data.forEach(function(entry) {
            chartData.push([new Date(entry.Date), entry.Humidity]);
        });

        var dataTable = google.visualization.arrayToDataTable(chartData);

        var options = {
            title: 'Humidity Chart',
            curveType: 'function',
            legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('humidity_chart'));
        chart.draw(dataTable, options);
    });
}
