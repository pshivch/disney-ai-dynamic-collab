import org.knowm.xchart.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        double[] xData = new double[] {0.0, 1.0, 2.0};
        double[] yData = new double[] {2.0, 1.0, 0.0};
        XYChart chart = QuickChart.getChart("Game Theory Negotiation", "X", "Y", "y(x)", xData, yData);
        new SwingWrapper<>(chart).displayChart();
    }
}