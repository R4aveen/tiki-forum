import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import { connect } from "react-redux";


function FullWidthLayout({
  children
}) {
  return (
    <div>
      <Navbar />

      <div className="flex">
        {/* aqui podria ir un <Sidebar/> */}
        <div className=" w-full md:pt-16 lg:pt-16 xl:pt-16 px-2">
          {children}
        </div>
      </div>
      
      <Footer />
    </div>
  );
}

const mapStateToProps = state =>({

})

export default connect(mapStateToProps,{

}) (FullWidthLayout)
