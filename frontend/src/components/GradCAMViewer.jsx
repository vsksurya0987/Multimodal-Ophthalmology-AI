function GradCAMViewer({ image }) {

    return (

        <div className="card">

            <h2>🔥 Grad-CAM Heatmap</h2>

            <img
                src={image}
                alt="GradCAM"
                className="gradcam-image"
            />

        </div>

    );

}

export default GradCAMViewer;