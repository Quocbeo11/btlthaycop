document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => item.timestamp); // Chỉnh sửa tên cột theo dữ liệu của bạn
            const values = data.map(item => item.temperature); // Chỉnh sửa tên cột theo dữ liệu của bạn

            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'bar', // Thay đổi loại biểu đồ nếu cần
                data: {
                    labels: labels,
                    datasets: [{
                        label: '# of Votes',
                        data: values,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});
