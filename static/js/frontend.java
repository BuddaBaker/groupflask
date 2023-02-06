import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class JeopardyGame extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        Label questionLabel = new Label();
        Button answerButton = new Button("Show Answer");

        VBox root = new VBox();
        root.setPadding(new Insets(10));
        root.setSpacing(10);
        root.getChildren().addAll(questionLabel, answerButton);

        Scene scene = new Scene(root, 300, 250);

        primaryStage.setTitle("Jeopardy");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}