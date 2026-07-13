function ReportButton({ report }) {

    return (

        <div className="card">

            <h2>📄 Medical Report</h2>

            <a

                href={report}

                download="Medical_Report.pdf"

            >

                <button>

                    Download Report

                </button>

            </a>

        </div>

    );

}

export default ReportButton;