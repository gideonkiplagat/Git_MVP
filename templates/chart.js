var chartType = 'line'; // Default chart type

// Function to change chart type
function changeChartType(type) {
    chartType = type;
    updateChart();
}

// Function to update chart with selected type
function updateChart() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: chartType,
        data: {
            labels: ['Commit 1', 'Commit 2', 'Commit 3'],
            datasets: [{
                label: 'Commit History',
                data: [3, 2, 1],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                ],
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
}

// Initial chart creation
updateChart();
