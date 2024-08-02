import './Home.css';
import ImageContainer from './components/Image';

function Home() {
    return (
        <div className="home">
            <ImageContainer god="/Belona.png" god_alt="Belona" class="warrior.png" class_alt="Warrior" color='#BE3C21'/>
            <ImageContainer god="/Pele.png" god_alt="Pele" class="Assassin.png" class_alt="Assassin" color='#EFB203'/>
            <ImageContainer god="/Anhur.png" god_alt="Anhur" class="Hunter.png" class_alt="Hunter" color='#E75900'/>
            <ImageContainer god="/Scylla.jpg" god_alt="Scylla" class="Mage.png" class_alt="Mage" color='#942591'/>
            <ImageContainer god="/Kuzenbo.jpg" god_alt="Kuzenbo" class="Guardian.png" class_alt="Guardian" color='#648921'/>
        </div>
    );
}

export default Home;
