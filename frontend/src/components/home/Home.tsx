import './Home.css';
import ImageContainer from './components/Image';

function Home() {
    return (
        <div className="home">
            <ImageContainer 
                god="/Belona.png" 
                god_alt="Belona" 
                class="warrior.png" 
                class_alt="Warrior" 
                color='#BE3C21'
                text='Warriors'
                text_color='#BE3C21'
                link='/warrior'
            />
            <ImageContainer 
                god="/Pele.png" 
                god_alt="Pele" 
                class="Assassin.png" 
                class_alt="Assassin" 
                color='#EFB203'
                text='Assassins'
                text_color='#EFB203'
                link='assassin'
            />
            <ImageContainer 
                god="/Anhur.png" 
                god_alt="Anhur" 
                class="Hunter.png" 
                class_alt="Hunter" 
                color='#E75900'
                text='Hunters'
                text_color='#E75900'
                link='/carry'
            />
            <ImageContainer 
                god="/Scylla.jpg" 
                god_alt="Scylla" 
                class="Mage.png" 
                class_alt="Mage" 
                color='#942591'
                text='Mages'
                text_color='#942591'
                link='mage'
            />
            <ImageContainer 
                god="/Kuzenbo.jpg" 
                god_alt="Kuzenbo" 
                class="Guardian.png" 
                class_alt="Guardian" 
                color='#648921'
                text='Guardians'
                text_color='#648921'   
                link='guardian'             
            />
        </div>
    );
}

export default Home;
