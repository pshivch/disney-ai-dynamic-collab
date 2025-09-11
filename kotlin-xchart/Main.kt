import org.knowm.xchart.*

fun main() {
    val xData = doubleArrayOf(0.0, 1.0, 2.0)
    val yData = doubleArrayOf(2.0, 1.0, 0.0)
    val chart = QuickChart.getChart("Scene Adaptation", "X", "Y", "y(x)", xData, yData)
    SwingWrapper(chart).displayChart()
}
