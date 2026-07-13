function UploadSection({

    image,

    setImage,

    analyzeImage,

    loading

}) {

    return (

        <div className="card">

            <h2>

                📷 Upload Retinal Image

            </h2>

            <input

                type="file"

                accept="image/*"

                onChange={(e) =>

                    setImage(e.target.files[0])

                }

            />

            <br /><br />

            {

                image &&

                <p>

                    Selected File:

                    <b>

                        {" "}

                        {image.name}

                    </b>

                </p>

            }

            <button

                onClick={analyzeImage}

                disabled={loading}

            >

                {

                    loading

                        ? "Analyzing..."

                        : "Analyze Image"

                }

            </button>

        </div>

    );

}

export default UploadSection;