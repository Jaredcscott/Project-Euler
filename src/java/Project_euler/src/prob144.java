
import java.math.BigDecimal;
import java.util.ArrayList;
import javafx.application.Application;
import javafx.geometry.Point2D;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jareds
 */
public class prob144 extends Application {
    Scene scene;
    
    public void start(Stage primaryStage) {
        Pane pane = new Pane();
        ArrayList<Point> toPlot = getPoints(-5.2,5.2,-10.1,10.1);
        for (Point point : toPlot) {
            pane.getChildren().add(new Circle(point.x,point.y,1));
        }
        
        scene = new Scene(pane, 1000, 750);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    
    public static class Point {
        double x;
        double y;
        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public static ArrayList<Point> getPoints(double minX, double maxX, double minY, double maxY) {
        ArrayList<Point> points = new ArrayList<Point>();
        for(double x = minX; x <= maxX; x += .001) {
            x = Math.round(x * 1000.0) / 1000.0;
            for ( double y = minY; y <= maxY ; y += .001) {
                y = Math.round(y * 1000.0) / 1000.0;
                //System.out.println("X: " + x + " Y: " + y);
                if ( ((4 *(Math.pow(x, 2))) + (Math.pow(y,2)))  == 100) {
                    System.out.println("X: " + x + " Y: " + y);
                    Point newPoint = new Point((x*10) + 150, (y*10) + 150);
                    points.add(newPoint);
                }
                
            }
            
        }
        //System.out.println(points.size());
        return points;
    }
    
    public static void main(String[] args) {
        launch(args);
    }
    
}
